# EMA Hourly Continuation — XLM/USDT P34_55

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6600 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.8711 |
| sortino_ratio | -0.4426 |
| max_drawdown | 0.4136 |
| cagr | -0.1829 |
| net_avg_win | 55.9645 |
| net_avg_loss | -89.3213 |
| avg_hold_time_bars | 6.5167 |
| exposure | 0.0797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
