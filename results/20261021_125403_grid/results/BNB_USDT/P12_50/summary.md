# EMA Hourly Continuation — BNB/USDT P12_50

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.5845 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -4.3889 |
| sortino_ratio | -1.5071 |
| max_drawdown | 0.8307 |
| cagr | -0.5003 |
| net_avg_win | 42.4983 |
| net_avg_loss | -67.0639 |
| avg_hold_time_bars | 11.6626 |
| exposure | 0.3016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
