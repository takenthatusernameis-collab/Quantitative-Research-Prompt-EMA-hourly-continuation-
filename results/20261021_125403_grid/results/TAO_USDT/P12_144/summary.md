# EMA Hourly Continuation — TAO/USDT P12_144

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8495 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.0337 |
| sortino_ratio | -0.2862 |
| max_drawdown | 0.3706 |
| cagr | -0.1259 |
| net_avg_win | 87.4645 |
| net_avg_loss | -99.7284 |
| avg_hold_time_bars | 37.6489 |
| exposure | 0.6435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
