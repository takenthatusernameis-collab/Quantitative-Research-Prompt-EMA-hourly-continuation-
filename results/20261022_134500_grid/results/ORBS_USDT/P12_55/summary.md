# EMA Hourly Continuation — ORBS/USDT P12_55

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.4612 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -9.1448 |
| sortino_ratio | -4.2126 |
| max_drawdown | 0.9949 |
| cagr | -0.8772 |
| net_avg_win | 19.3058 |
| net_avg_loss | -29.0744 |
| avg_hold_time_bars | 8.3783 |
| exposure | 0.4098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
