# EMA Hourly Continuation — JTO/USDT P34_89

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -4.5339 |
| sortino_ratio | -1.6851 |
| max_drawdown | 0.8740 |
| cagr | -0.5522 |
| net_avg_win | 40.1313 |
| net_avg_loss | -56.3994 |
| avg_hold_time_bars | 7.3438 |
| exposure | 0.2330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
