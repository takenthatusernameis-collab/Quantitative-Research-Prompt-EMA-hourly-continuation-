# EMA Hourly Continuation — COMP/USDT P8_89

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.7830 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -1.6565 |
| sortino_ratio | -0.5456 |
| max_drawdown | 0.5071 |
| cagr | -0.2241 |
| net_avg_win | 62.7420 |
| net_avg_loss | -83.8434 |
| avg_hold_time_bars | 27.4170 |
| exposure | 0.6605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
