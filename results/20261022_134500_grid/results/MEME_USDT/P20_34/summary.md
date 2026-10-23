# EMA Hourly Continuation — MEME/USDT P20_34

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1175 |
| net_profit_factor | 0.3847 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -9.6477 |
| sortino_ratio | -4.7020 |
| max_drawdown | 0.9969 |
| cagr | -0.8993 |
| net_avg_win | 12.4912 |
| net_avg_loss | -23.9670 |
| avg_hold_time_bars | 2.8528 |
| exposure | 0.1524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
