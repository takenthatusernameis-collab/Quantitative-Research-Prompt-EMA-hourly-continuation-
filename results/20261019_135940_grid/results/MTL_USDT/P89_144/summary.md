# EMA Hourly Continuation — MTL/USDT P89_144

**Symbol:** MTL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.4001 |
| net_win_rate | 0.4158 |
| gross_profit_factor | 0.7570 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -5.9087 |
| sortino_ratio | -1.7803 |
| max_drawdown | 0.8913 |
| cagr | -0.5851 |
| net_avg_win | 31.2894 |
| net_avg_loss | -55.6481 |
| avg_hold_time_bars | 7.9847 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
