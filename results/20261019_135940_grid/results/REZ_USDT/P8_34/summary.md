# EMA Hourly Continuation — REZ/USDT P8_34

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1269 |
| net_profit_factor | 0.6927 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 1.0472 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -5.5060 |
| sortino_ratio | -2.7826 |
| max_drawdown | 0.9653 |
| cagr | -0.7354 |
| net_avg_win | 35.5233 |
| net_avg_loss | -47.6172 |
| avg_hold_time_bars | 6.1458 |
| exposure | 0.3598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
