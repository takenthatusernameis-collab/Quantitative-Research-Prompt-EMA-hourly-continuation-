# EMA Hourly Continuation — WIN/USDT P20_144

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8251 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -4.2741 |
| sortino_ratio | -1.2991 |
| max_drawdown | 0.8065 |
| cagr | -0.4685 |
| net_avg_win | 36.4354 |
| net_avg_loss | -62.5108 |
| avg_hold_time_bars | 25.0837 |
| exposure | 0.5313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
