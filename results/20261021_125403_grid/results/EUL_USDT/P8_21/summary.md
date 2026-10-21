# EMA Hourly Continuation — EUL/USDT P8_21

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.6394 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -3.1732 |
| sortino_ratio | -1.1167 |
| max_drawdown | 0.7443 |
| cagr | -0.4009 |
| net_avg_win | 44.5643 |
| net_avg_loss | -62.9212 |
| avg_hold_time_bars | 7.5717 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
