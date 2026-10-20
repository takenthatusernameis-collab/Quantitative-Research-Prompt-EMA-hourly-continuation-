# EMA Hourly Continuation — AVA/USDT P21_55

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.4632 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8559 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -6.8256 |
| sortino_ratio | -2.9409 |
| max_drawdown | 0.9747 |
| cagr | -0.7652 |
| net_avg_win | 19.3563 |
| net_avg_loss | -35.9167 |
| avg_hold_time_bars | 4.8935 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
