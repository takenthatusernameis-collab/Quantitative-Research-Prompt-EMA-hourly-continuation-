# EMA Hourly Continuation — BOME/USDT P20_144

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6932 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9253 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.1587 |
| sortino_ratio | -0.6393 |
| max_drawdown | 0.5703 |
| cagr | -0.2638 |
| net_avg_win | 56.1263 |
| net_avg_loss | -76.3681 |
| avg_hold_time_bars | 28.4157 |
| exposure | 0.5748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
