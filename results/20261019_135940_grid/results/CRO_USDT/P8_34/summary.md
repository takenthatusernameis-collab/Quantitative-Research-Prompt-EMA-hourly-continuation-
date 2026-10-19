# EMA Hourly Continuation — CRO/USDT P8_34

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1444 |
| net_profit_factor | 0.3548 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -11.6728 |
| sortino_ratio | -6.2711 |
| max_drawdown | 0.9997 |
| cagr | -0.9583 |
| net_avg_win | 9.1761 |
| net_avg_loss | -18.3350 |
| avg_hold_time_bars | 5.1094 |
| exposure | 0.3354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
