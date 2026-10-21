# EMA Hourly Continuation — ETH/USDT P50_144

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6828 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.8354 |
| sortino_ratio | -0.4541 |
| max_drawdown | 0.4392 |
| cagr | -0.1878 |
| net_avg_win | 58.7862 |
| net_avg_loss | -86.6784 |
| avg_hold_time_bars | 17.3535 |
| exposure | 0.2343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
