# EMA Hourly Continuation — LUNA/USDT P8_55

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1242 |
| net_profit_factor | 0.4905 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.8371 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -9.2138 |
| sortino_ratio | -4.5611 |
| max_drawdown | 0.9965 |
| cagr | -0.8949 |
| net_avg_win | 18.5204 |
| net_avg_loss | -27.0147 |
| avg_hold_time_bars | 8.0749 |
| exposure | 0.4559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
