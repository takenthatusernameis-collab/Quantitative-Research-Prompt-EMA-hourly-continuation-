# EMA Hourly Continuation — ETH/USDT P34_144

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.5542 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7760 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -2.7651 |
| sortino_ratio | -0.6351 |
| max_drawdown | 0.5484 |
| cagr | -0.2543 |
| net_avg_win | 55.8786 |
| net_avg_loss | -80.6584 |
| avg_hold_time_bars | 38.6552 |
| exposure | 0.4586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
