# EMA Hourly Continuation — XLM/USDT P12_21

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1586 |
| net_profit_factor | 0.0965 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.5478 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -16.2651 |
| sortino_ratio | -9.3611 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 1.7865 |
| net_avg_loss | -11.2027 |
| avg_hold_time_bars | 2.1551 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
