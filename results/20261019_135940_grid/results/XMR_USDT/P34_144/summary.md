# EMA Hourly Continuation — XMR/USDT P34_144

**Symbol:** XMR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.4410 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -6.9878 |
| sortino_ratio | -2.8093 |
| max_drawdown | 0.9700 |
| cagr | -0.7507 |
| net_avg_win | 21.4826 |
| net_avg_loss | -37.3760 |
| avg_hold_time_bars | 9.3732 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
