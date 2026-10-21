# EMA Hourly Continuation — CFX/USDT P50_200

**Symbol:** CFX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8305 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0085 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -0.9717 |
| sortino_ratio | -0.2319 |
| max_drawdown | 0.2712 |
| cagr | -0.1023 |
| net_avg_win | 83.0749 |
| net_avg_loss | -101.4770 |
| avg_hold_time_bars | 30.3597 |
| exposure | 0.3836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
