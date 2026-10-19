# EMA Hourly Continuation — BONK/USDT P12_26

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1412 |
| net_profit_factor | 0.5040 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -9.9893 |
| sortino_ratio | -5.2880 |
| max_drawdown | 0.9987 |
| cagr | -0.9283 |
| net_avg_win | 16.8548 |
| net_avg_loss | -24.8558 |
| avg_hold_time_bars | 2.7840 |
| exposure | 0.1787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
