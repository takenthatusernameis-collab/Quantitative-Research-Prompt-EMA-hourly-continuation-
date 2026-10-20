# EMA Hourly Continuation — PEOPLE/USDT P20_26

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1160 |
| net_profit_factor | 0.3382 |
| net_win_rate | 0.3966 |
| gross_profit_factor | 0.7057 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -11.6943 |
| sortino_ratio | -5.6841 |
| max_drawdown | 0.9994 |
| cagr | -0.9459 |
| net_avg_win | 11.1012 |
| net_avg_loss | -21.5716 |
| avg_hold_time_bars | 2.2164 |
| exposure | 0.1163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
