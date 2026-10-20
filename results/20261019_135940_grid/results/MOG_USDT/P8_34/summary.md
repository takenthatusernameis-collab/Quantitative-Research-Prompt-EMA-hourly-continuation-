# EMA Hourly Continuation — MOG/USDT P8_34

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1227 |
| net_profit_factor | 0.6918 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9698 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -5.2905 |
| sortino_ratio | -2.7350 |
| max_drawdown | 0.9496 |
| cagr | -0.7277 |
| net_avg_win | 35.9409 |
| net_avg_loss | -48.5942 |
| avg_hold_time_bars | 5.8346 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
