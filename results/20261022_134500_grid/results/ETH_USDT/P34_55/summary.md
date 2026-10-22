# EMA Hourly Continuation — ETH/USDT P34_55

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.2258 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.7779 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -11.4489 |
| sortino_ratio | -4.9101 |
| max_drawdown | 0.9985 |
| cagr | -0.9252 |
| net_avg_win | 8.6414 |
| net_avg_loss | -24.1522 |
| avg_hold_time_bars | 3.3628 |
| exposure | 0.1331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
