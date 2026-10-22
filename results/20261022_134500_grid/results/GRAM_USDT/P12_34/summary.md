# EMA Hourly Continuation — GRAM/USDT P12_34

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.3687 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -11.8401 |
| sortino_ratio | -6.1177 |
| max_drawdown | 0.9997 |
| cagr | -0.9586 |
| net_avg_win | 10.3867 |
| net_avg_loss | -20.3260 |
| avg_hold_time_bars | 3.7062 |
| exposure | 0.2259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
