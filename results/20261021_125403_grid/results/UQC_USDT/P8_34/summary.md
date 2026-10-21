# EMA Hourly Continuation — UQC/USDT P8_34

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.4372 |
| net_win_rate | 0.3516 |
| gross_profit_factor | 0.6714 |
| gross_win_rate | 0.3631 |
| sharpe_ratio | -5.3463 |
| sortino_ratio | -1.3920 |
| max_drawdown | 0.8174 |
| cagr | -0.4855 |
| net_avg_win | 51.7543 |
| net_avg_loss | -64.1932 |
| avg_hold_time_bars | 36.9164 |
| exposure | 0.5798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
