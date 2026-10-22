# EMA Hourly Continuation — KNC/USDT P50_89

**Symbol:** KNC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9701 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -3.2545 |
| sortino_ratio | -0.9712 |
| max_drawdown | 0.7058 |
| cagr | -0.3576 |
| net_avg_win | 57.3299 |
| net_avg_loss | -83.1866 |
| avg_hold_time_bars | 7.1157 |
| exposure | 0.1397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
