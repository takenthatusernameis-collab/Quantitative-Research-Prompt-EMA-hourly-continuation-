# EMA Hourly Continuation — STX/USDT P21_144

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6924 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.3566 |
| sortino_ratio | -0.7182 |
| max_drawdown | 0.6133 |
| cagr | -0.2878 |
| net_avg_win | 56.2896 |
| net_avg_loss | -78.5671 |
| avg_hold_time_bars | 26.1667 |
| exposure | 0.5541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
