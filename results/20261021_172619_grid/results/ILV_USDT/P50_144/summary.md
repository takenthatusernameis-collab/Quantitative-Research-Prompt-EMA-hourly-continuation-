# EMA Hourly Continuation — ILV/USDT P50_144

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8487 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -0.9671 |
| sortino_ratio | -0.2592 |
| max_drawdown | 0.2997 |
| cagr | -0.1135 |
| net_avg_win | 81.7912 |
| net_avg_loss | -102.6822 |
| avg_hold_time_bars | 17.6427 |
| exposure | 0.2783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
