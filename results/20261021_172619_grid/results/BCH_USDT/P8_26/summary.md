# EMA Hourly Continuation — BCH/USDT P8_26

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.2725 |
| sortino_ratio | -1.1251 |
| max_drawdown | 0.7375 |
| cagr | -0.4004 |
| net_avg_win | 43.7849 |
| net_avg_loss | -66.5237 |
| avg_hold_time_bars | 8.0209 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
