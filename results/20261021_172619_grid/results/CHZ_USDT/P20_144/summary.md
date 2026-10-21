# EMA Hourly Continuation — CHZ/USDT P20_144

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.9322 |
| net_win_rate | 0.5313 |
| gross_profit_factor | 1.1325 |
| gross_win_rate | 0.5313 |
| sharpe_ratio | -0.3654 |
| sortino_ratio | -0.0965 |
| max_drawdown | 0.3164 |
| cagr | -0.0479 |
| net_avg_win | 89.4494 |
| net_avg_loss | -108.7944 |
| avg_hold_time_bars | 37.2149 |
| exposure | 0.5667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
