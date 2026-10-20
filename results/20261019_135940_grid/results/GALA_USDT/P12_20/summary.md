# EMA Hourly Continuation — GALA/USDT P12_20

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1482 |
| net_profit_factor | 0.2918 |
| net_win_rate | 0.3866 |
| gross_profit_factor | 0.6887 |
| gross_win_rate | 0.4143 |
| sharpe_ratio | -13.7798 |
| sortino_ratio | -7.5989 |
| max_drawdown | 0.9999 |
| cagr | -0.9795 |
| net_avg_win | 7.1887 |
| net_avg_loss | -15.5320 |
| avg_hold_time_bars | 2.1930 |
| exposure | 0.1477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
