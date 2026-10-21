# EMA Hourly Continuation — AERO/USDT P12_89

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.9716 |
| net_win_rate | 0.5351 |
| gross_profit_factor | 1.1378 |
| gross_win_rate | 0.5351 |
| sharpe_ratio | -0.1505 |
| sortino_ratio | -0.0486 |
| max_drawdown | 0.3252 |
| cagr | -0.0306 |
| net_avg_win | 96.1851 |
| net_avg_loss | -113.9301 |
| avg_hold_time_bars | 22.1443 |
| exposure | 0.5023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
