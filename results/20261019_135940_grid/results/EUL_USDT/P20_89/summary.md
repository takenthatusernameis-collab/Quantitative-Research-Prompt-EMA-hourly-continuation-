# EMA Hourly Continuation — EUL/USDT P20_89

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.4806 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.7115 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -4.9530 |
| sortino_ratio | -1.8071 |
| max_drawdown | 0.8943 |
| cagr | -0.5838 |
| net_avg_win | 27.4271 |
| net_avg_loss | -44.8215 |
| avg_hold_time_bars | 12.0484 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
