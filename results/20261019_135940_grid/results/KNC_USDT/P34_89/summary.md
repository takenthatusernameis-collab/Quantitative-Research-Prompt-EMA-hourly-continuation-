# EMA Hourly Continuation — KNC/USDT P34_89

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5831 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -4.9829 |
| sortino_ratio | -1.7635 |
| max_drawdown | 0.8906 |
| cagr | -0.5773 |
| net_avg_win | 41.2634 |
| net_avg_loss | -63.3692 |
| avg_hold_time_bars | 9.0819 |
| exposure | 0.2621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
