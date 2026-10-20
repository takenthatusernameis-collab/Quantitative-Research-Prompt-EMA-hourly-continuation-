# EMA Hourly Continuation — SUPER/USDT P26_34

**Symbol:** SUPER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.2853 |
| net_win_rate | 0.4013 |
| gross_profit_factor | 0.6685 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -11.1761 |
| sortino_ratio | -5.2303 |
| max_drawdown | 0.9988 |
| cagr | -0.9310 |
| net_avg_win | 9.2916 |
| net_avg_loss | -21.8343 |
| avg_hold_time_bars | 2.5734 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
