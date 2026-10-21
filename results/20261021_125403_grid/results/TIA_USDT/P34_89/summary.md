# EMA Hourly Continuation — TIA/USDT P34_89

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.8903 |
| net_win_rate | 0.5224 |
| gross_profit_factor | 1.0910 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -0.7501 |
| sortino_ratio | -0.2227 |
| max_drawdown | 0.2981 |
| cagr | -0.1008 |
| net_avg_win | 85.6121 |
| net_avg_loss | -105.1613 |
| avg_hold_time_bars | 11.5953 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
