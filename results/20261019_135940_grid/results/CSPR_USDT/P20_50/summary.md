# EMA Hourly Continuation — CSPR/USDT P20_50

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1286 |
| net_profit_factor | 0.3485 |
| net_win_rate | 0.3896 |
| gross_profit_factor | 0.7182 |
| gross_win_rate | 0.4067 |
| sharpe_ratio | -11.0793 |
| sortino_ratio | -5.5988 |
| max_drawdown | 0.9992 |
| cagr | -0.9408 |
| net_avg_win | 10.6670 |
| net_avg_loss | -19.5362 |
| avg_hold_time_bars | 3.7107 |
| exposure | 0.2169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
