# EMA Hourly Continuation — PEOPLE/USDT P8_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.6038 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8708 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -5.5329 |
| sortino_ratio | -2.4262 |
| max_drawdown | 0.9448 |
| cagr | -0.6829 |
| net_avg_win | 32.7202 |
| net_avg_loss | -44.6539 |
| avg_hold_time_bars | 11.4805 |
| exposure | 0.5060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
