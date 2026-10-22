# EMA Hourly Continuation — BICO/USDT P34_200

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6783 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.7947 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -2.1042 |
| sortino_ratio | -0.5206 |
| max_drawdown | 0.4766 |
| cagr | -0.2142 |
| net_avg_win | 69.8821 |
| net_avg_loss | -83.0254 |
| avg_hold_time_bars | 37.0554 |
| exposure | 0.5171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
