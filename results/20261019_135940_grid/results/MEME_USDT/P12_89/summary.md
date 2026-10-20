# EMA Hourly Continuation — MEME/USDT P12_89

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6469 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -3.6720 |
| sortino_ratio | -1.3110 |
| max_drawdown | 0.8090 |
| cagr | -0.4675 |
| net_avg_win | 47.5628 |
| net_avg_loss | -65.7897 |
| avg_hold_time_bars | 20.1373 |
| exposure | 0.5931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
