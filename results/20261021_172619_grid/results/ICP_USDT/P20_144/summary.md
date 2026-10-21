# EMA Hourly Continuation — ICP/USDT P20_144

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.9151 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.0966 |
| gross_win_rate | 0.5268 |
| sharpe_ratio | -0.4529 |
| sortino_ratio | -0.1195 |
| max_drawdown | 0.2190 |
| cagr | -0.0574 |
| net_avg_win | 83.9270 |
| net_avg_loss | -102.1001 |
| avg_hold_time_bars | 37.6488 |
| exposure | 0.5750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
