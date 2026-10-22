# EMA Hourly Continuation — CTSI/USDT P8_20

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.6938 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -3.6182 |
| sortino_ratio | -1.3981 |
| max_drawdown | 0.7988 |
| cagr | -0.4719 |
| net_avg_win | 51.1364 |
| net_avg_loss | -70.1357 |
| avg_hold_time_bars | 5.7259 |
| exposure | 0.1890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
