# EMA Hourly Continuation — ARKM/USDT P8_144

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8444 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9716 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -0.8969 |
| sortino_ratio | -0.2365 |
| max_drawdown | 0.2988 |
| cagr | -0.1055 |
| net_avg_win | 77.9875 |
| net_avg_loss | -91.8153 |
| avg_hold_time_bars | 49.2962 |
| exposure | 0.7641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
