# EMA Hourly Continuation — BTT/USDT P21_34

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.1401 |
| net_win_rate | 0.2639 |
| gross_profit_factor | 0.5330 |
| gross_win_rate | 0.3570 |
| sharpe_ratio | -18.6737 |
| sortino_ratio | -9.8687 |
| max_drawdown | 1.0000 |
| cagr | -0.9958 |
| net_avg_win | 5.2746 |
| net_avg_loss | -13.4917 |
| avg_hold_time_bars | 2.8898 |
| exposure | 0.1538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
