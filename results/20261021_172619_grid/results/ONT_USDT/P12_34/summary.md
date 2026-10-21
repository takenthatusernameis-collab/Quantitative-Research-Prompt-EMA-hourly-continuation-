# EMA Hourly Continuation — ONT/USDT P12_34

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.6869 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -3.1171 |
| sortino_ratio | -1.1250 |
| max_drawdown | 0.7475 |
| cagr | -0.4019 |
| net_avg_win | 51.0864 |
| net_avg_loss | -71.3969 |
| avg_hold_time_bars | 6.3234 |
| exposure | 0.1823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
