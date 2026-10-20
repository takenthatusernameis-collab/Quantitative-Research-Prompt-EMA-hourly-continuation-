# EMA Hourly Continuation — TFUEL/USDT P20_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.4397 |
| net_win_rate | 0.3919 |
| gross_profit_factor | 0.7924 |
| gross_win_rate | 0.4177 |
| sharpe_ratio | -10.1700 |
| sortino_ratio | -4.7165 |
| max_drawdown | 0.9973 |
| cagr | -0.9042 |
| net_avg_win | 18.4551 |
| net_avg_loss | -27.0487 |
| avg_hold_time_bars | 5.3965 |
| exposure | 0.2642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
