# EMA Hourly Continuation — ZRO/USDT P89_144

**Symbol:** ZRO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.2490 |
| sortino_ratio | -0.2742 |
| max_drawdown | 0.2964 |
| cagr | -0.1189 |
| net_avg_win | 71.5731 |
| net_avg_loss | -91.1967 |
| avg_hold_time_bars | 6.9543 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
