# EMA Hourly Continuation — MOVR/USDT P8_89

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.6929 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8472 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.6746 |
| sortino_ratio | -0.8980 |
| max_drawdown | 0.6512 |
| cagr | -0.3384 |
| net_avg_win | 56.6920 |
| net_avg_loss | -69.3930 |
| avg_hold_time_bars | 24.3143 |
| exposure | 0.6189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
