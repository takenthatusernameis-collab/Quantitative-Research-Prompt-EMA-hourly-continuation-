# EMA Hourly Continuation — ICP/USDT P50_144

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5952 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -3.7973 |
| sortino_ratio | -1.2064 |
| max_drawdown | 0.7778 |
| cagr | -0.4407 |
| net_avg_win | 46.2595 |
| net_avg_loss | -71.0247 |
| avg_hold_time_bars | 12.5303 |
| exposure | 0.2910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
