# EMA Hourly Continuation — CHZ/USDT P20_200

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.5478 |
| gross_profit_factor | 1.2273 |
| gross_win_rate | 0.5507 |
| sharpe_ratio | -0.8214 |
| sortino_ratio | -0.2162 |
| max_drawdown | 0.3690 |
| cagr | -0.1002 |
| net_avg_win | 78.8618 |
| net_avg_loss | -110.4712 |
| avg_hold_time_bars | 41.9652 |
| exposure | 0.6581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
