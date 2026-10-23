# EMA Hourly Continuation — MOCA/USDT P20_144

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6077 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -3.6753 |
| sortino_ratio | -1.1121 |
| max_drawdown | 0.7180 |
| cagr | -0.4210 |
| net_avg_win | 55.9696 |
| net_avg_loss | -78.2083 |
| avg_hold_time_bars | 25.8998 |
| exposure | 0.5570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
