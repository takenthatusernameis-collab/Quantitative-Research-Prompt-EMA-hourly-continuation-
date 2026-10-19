# EMA Hourly Continuation — NFT/USDT P34_89

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1221 |
| net_profit_factor | 0.2522 |
| net_win_rate | 0.2219 |
| gross_profit_factor | 0.6511 |
| gross_win_rate | 0.2613 |
| sharpe_ratio | -20.0999 |
| sortino_ratio | -10.8614 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 12.4447 |
| net_avg_loss | -14.0763 |
| avg_hold_time_bars | 5.7027 |
| exposure | 0.3165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
