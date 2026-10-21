# EMA Hourly Continuation — LDO/USDT P89_144

**Symbol:** LDO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6716 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.8711 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -2.0097 |
| sortino_ratio | -0.4684 |
| max_drawdown | 0.4457 |
| cagr | -0.1930 |
| net_avg_win | 68.1448 |
| net_avg_loss | -89.3145 |
| avg_hold_time_bars | 8.0787 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
