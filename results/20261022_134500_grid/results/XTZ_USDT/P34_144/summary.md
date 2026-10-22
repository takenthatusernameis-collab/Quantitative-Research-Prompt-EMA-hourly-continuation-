# EMA Hourly Continuation — XTZ/USDT P34_144

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7513 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1876 |
| gross_win_rate | 0.5394 |
| sharpe_ratio | -2.0436 |
| sortino_ratio | -0.6474 |
| max_drawdown | 0.5607 |
| cagr | -0.2621 |
| net_avg_win | 61.7825 |
| net_avg_loss | -91.7240 |
| avg_hold_time_bars | 18.5515 |
| exposure | 0.4174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
